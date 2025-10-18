from setuptools import setup, find_packages

setup(
    name="bot-project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # أضف المتطلبات هنا إذا كان لديك
        "numpy",
        "pandas",
    ],
    python_requires=">=3.10",
)
