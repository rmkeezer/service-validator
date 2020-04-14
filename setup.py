from setuptools import setup, find_packages

setup(
    name="schemathesis_ibm",
    version="0.0.1",
    description="Python package, Schemathesis, extended to include IBM API Handbook validation.",
    url="https://github.ibm.com/CloudEngineering/schemathesis-endpoint-validator",
    author="Barrett Schonefeld, IBM",
    author_email="barrett.schonefeld@ibm.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["click", "schemathesis"],
    entry_points="""
        [console_scripts]
        schemathesis-ibm=schemathesis_ibm.cli.run_schemathesis:run_schemathesis
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)