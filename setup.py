import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="MailboxValidator",
	version="1.3.1",
	author="MailboxValidator.com",
	author_email="support@mailboxvalidator.com",
	description="Email verification module for Python using MailboxValidator API. It validates if the email is valid, from a free provider, contains high-risk keywords, whether it\'s a catch-all address and so much more.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/MailboxValidator/mailboxvalidator-python",
	packages=setuptools.find_packages(),
	tests_require=['pytest>=3.0.6'],
	classifiers=(
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	),
)