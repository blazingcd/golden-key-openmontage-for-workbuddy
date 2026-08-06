from setuptools import setup, find_packages

setup(
    name="golden-key-openmontage-workbuddy",
    version="0.1.0a0",
    description="Golden Key OpenMontage callable core for WorkBuddy",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "pyyaml>=6.0",
        "pydantic>=2.0",
        "jsonschema>=4.20",
        "python-dotenv>=1.0",
        "Pillow>=10.0",
        "requests>=2.31",
        "httpx>=0.28,<1",
        "google-genai>=1.0.0",
        "openai>=2.44.0",
    ],
    entry_points={
        "console_scripts": [
            "golden-key-workbuddy=golden_key_openmontage_workbuddy.cli:main",
        ],
    },
)
