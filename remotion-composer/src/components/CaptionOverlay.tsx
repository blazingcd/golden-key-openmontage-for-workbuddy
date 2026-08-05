import {
  AbsoluteFill,
  Sequence,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import {Fragment} from "react";

// Word-level caption for TikTok-style highlight display
export interface WordCaption {
  word: string;
  startMs: number;
  endMs: number;
  // Optional Director-authored layout boundaries. When pageId is present,
  // semantic pages take precedence over the generic wordsPerPage fallback.
  pageId?: string;
  lineBreakAfter?: boolean;
}

type CaptionOverlayProps = {
  words: WordCaption[];
  // How many words to show at once in a "page"
  wordsPerPage?: number;
  fontSize?: number;
  color?: string;
  highlightColor?: string;
  backgroundColor?: string;
  fontFamily?: string;
};

interface CaptionPage {
  words: WordCaption[];
  startMs: number;
  endMs: number;
}

const CJK_CHARACTER = /[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]/u;
const CJK_PUNCTUATION = /[，。！？、；：]/u;

function captionSeparator(current: string, next: string | undefined): string {
  if (!next) return "";
  const currentTail = current.trim().slice(-1);
  const nextHead = next.trim().slice(0, 1);
  const joinsCjk =
    (CJK_CHARACTER.test(currentTail) || CJK_PUNCTUATION.test(currentTail)) &&
    (CJK_CHARACTER.test(nextHead) || CJK_PUNCTUATION.test(nextHead));
  return joinsCjk ? "" : " ";
}

function buildPages(words: WordCaption[], wordsPerPage: number): CaptionPage[] {
  const hasExplicitPages = words.length > 0 && words.every((word) => word.pageId);
  if (hasExplicitPages) {
    const pages: CaptionPage[] = [];
    for (const word of words) {
      const current = pages[pages.length - 1];
      if (!current || current.words[0].pageId !== word.pageId) {
        pages.push({words: [word], startMs: word.startMs, endMs: word.endMs});
      } else {
        current.words.push(word);
        current.endMs = word.endMs;
      }
    }
    return pages;
  }

  const pages: CaptionPage[] = [];
  for (let i = 0; i < words.length; i += wordsPerPage) {
    const pageWords = words.slice(i, i + wordsPerPage);
    if (pageWords.length === 0) continue;
    pages.push({
      words: pageWords,
      startMs: pageWords[0].startMs,
      endMs: pageWords[pageWords.length - 1].endMs,
    });
  }
  return pages;
}

function maxAuthoredLineLength(words: WordCaption[]): number {
  let current = 0;
  let maximum = 0;
  for (let i = 0; i < words.length; i++) {
    current += Array.from(words[i].word).length;
    const isPageEnd = words[i + 1]?.pageId !== words[i].pageId;
    if (
      !words[i].lineBreakAfter &&
      !isPageEnd &&
      captionSeparator(words[i].word, words[i + 1]?.word)
    ) {
      current += 1;
    }
    if (words[i].lineBreakAfter || isPageEnd || i === words.length - 1) {
      maximum = Math.max(maximum, current);
      current = 0;
    }
  }
  return maximum;
}

const PageRenderer: React.FC<{
  page: CaptionPage;
  fontSize: number;
  color: string;
  highlightColor: string;
  backgroundColor: string;
  fontFamily: string;
  lockAuthoredLineBreaks: boolean;
}> = ({
  page,
  fontSize,
  color,
  highlightColor,
  backgroundColor,
  fontFamily,
  lockAuthoredLineBreaks,
}) => {
  const frame = useCurrentFrame();
  const { fps, height } = useVideoConfig();

  const currentMs = page.startMs + (frame / fps) * 1000;

  // Spring entrance
  const entrance = spring({
    frame,
    fps,
    config: { damping: 18, stiffness: 120 },
  });

  return (
    <AbsoluteFill
      style={{
        justifyContent: "flex-end",
        alignItems: "center",
        // Keep the caption band in the lower quarter across output sizes.
        // A fixed pixel value was too low on 1080x1920 renders.
        paddingBottom: Math.round(height * 0.18),
      }}
    >
      <div
        style={{
          opacity: entrance,
          transform: `translateY(${interpolate(entrance, [0, 1], [20, 0])}px)`,
          backgroundColor,
          borderRadius: 12,
          padding: "14px 28px",
          maxWidth: "90%",
          textAlign: "center",
        }}
      >
        <span
          style={{
            fontSize,
            fontWeight: 700,
            fontFamily,
            lineHeight: 1.4,
            whiteSpace: lockAuthoredLineBreaks ? "nowrap" : "normal",
          }}
        >
          {page.words.map((w, i) => {
            const isActive = w.startMs <= currentMs && w.endMs > currentMs;
            const isPast = w.endMs <= currentMs;
            return (
              <Fragment key={`${w.startMs}-${i}`}>
                <span
                  style={{
                    display: "inline-block",
                    color: isActive ? highlightColor : isPast ? color : `${color}99`,
                    transition: "none", // CSS transitions forbidden in Remotion
                    textShadow: isActive
                      ? `0 0 20px ${highlightColor}66, 0 2px 4px rgba(0,0,0,0.5)`
                      : "0 2px 4px rgba(0,0,0,0.5)",
                  }}
                >
                  {w.word}{w.lineBreakAfter ? "" : captionSeparator(w.word, page.words[i + 1]?.word)}
                </span>
                {w.lineBreakAfter && i < page.words.length - 1 ? <br /> : null}
              </Fragment>
            );
          })}
        </span>
      </div>
    </AbsoluteFill>
  );
};

export const CaptionOverlay: React.FC<CaptionOverlayProps> = ({
  words,
  wordsPerPage = 6,
  fontSize = 42,
  color = "#F8FAFC",
  highlightColor = "#22D3EE",
  backgroundColor = "rgba(15, 23, 42, 0.75)",
  fontFamily = "Space Grotesk, Inter, system-ui, sans-serif",
}) => {
  const { fps, width } = useVideoConfig();
  const pages = buildPages(words, wordsPerPage);
  const hasExplicitLayout = words.length > 0 && words.every((word) => word.pageId);
  const authoredLineLength = hasExplicitLayout ? maxAuthoredLineLength(words) : 0;
  // Keep one stable font size across the whole asset. Explicit lines must fit
  // inside the 90% caption box (56px horizontal padding) without browser-made
  // third lines that contradict the Director layout.
  const fittedFontSize = hasExplicitLayout
    ? Math.min(
        fontSize,
        Math.floor(((width * 0.9 - 56) / Math.max(1, authoredLineLength)) * 0.96)
      )
    : fontSize;

  return (
    <AbsoluteFill>
      {pages.map((page, i) => {
        const fromFrame = Math.round((page.startMs / 1000) * fps);
        const nextStart = pages[i + 1]?.startMs ?? page.endMs + 500;
        const duration = Math.max(
          1,
          Math.round(((nextStart - page.startMs) / 1000) * fps)
        );

        return (
          <Sequence key={i} from={fromFrame} durationInFrames={duration}>
            <PageRenderer
              page={page}
              fontSize={fittedFontSize}
              color={color}
              highlightColor={highlightColor}
              backgroundColor={backgroundColor}
              fontFamily={fontFamily}
              lockAuthoredLineBreaks={hasExplicitLayout}
            />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
