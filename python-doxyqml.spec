Name: python-doxyqml
Version: 0.5.3
Release: 2
Source0: https://files.pythonhosted.org/packages/source/d/doxyqml/doxyqml-%{version}.tar.gz
Summary: Doxygen filter for documenting QML classes
URL: https://pypi.org/project/doxyqml/
License: BSD
Group: Development/Python
BuildRequires:	python-setuptools
BuildArch: noarch

%description
Doxyqml lets you use Doxygen to document your QML classes.

It integrates as a Doxygen input filter to turn .qml files
into pseudo-C++ which Doxygen can then use to generate
documentation.

%prep
%autosetup -p1 -n doxyqml-%{version}

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}

%files
%{_bindir}/doxyqml
%{_prefix}/lib/python*/site-packages/doxyqml-*.egg-info
%{_prefix}/lib/python*/site-packages/doxyqml
