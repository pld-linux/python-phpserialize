# Conditional build:
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		phpserialize
%define		egg_name	phpserialize
%define		pypi_name	phpserialize
Summary:	A port of the serialize and unserialize functions of php to python
Name:		python-%{pypi_name}
Version:	1.3
Release:	6
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.debian.net/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	cbf88a62e04135e3be3c7fe412525b8b
URL:		https://pypi.python.org/pypi/phpserialize
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A port of the serialize and unserialize functions of php to python.

%package -n python3-%{pypi_name}
Summary:	A port of the serialize and unserialize functions of php to python
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{pypi_name}
A port of the serialize and unserialize functions of php to python.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc PKG-INFO
%{py_sitescriptdir}/%{module}.py*
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc PKG-INFO
%{py3_sitescriptdir}/%{module}.py*
%{py3_sitescriptdir}/__pycache__/%{module}*
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
