Name:           tildejsongen
Version:        0.1.2
Release:        1%{?dist}
Summary:        An example Python application

License:        MIT
URL:            https://github.com/dimension-sh/tildejsongen
Source0:        https://github.com/dimension-sh/tildejsongen/archive/%{version}.tar.gz#/tildejsongen-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

Recommends: python3-pyyaml, python3-jinja2

%description
A Python application which provides a convenient example.


%prep
%autosetup -n tildejsongen-%{version}


%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test


%files
%license LICENSE
%doc README.md
%doc config-example.ini
%{python3_sitelib}/*
%{_bindir}/tildejsongen


%changelog
* Thu Jun 10 2021 Andrew Williams <andy@tensixtyone.com> 0.1.2-1
- Initial RPM package
