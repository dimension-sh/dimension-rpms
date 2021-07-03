Name:           simplelist
Version:        1.1.0
Release:        1%{?dist}
Summary:        An example Python application

License:        MIT
URL:            https://github.com/dimension-sh/simplelist
Source0:        https://github.com/dimension-sh/simplelist/archive/%{version}.tar.gz#/simplelist-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

Requires: python3-pyyaml

%description
A Python application which provides a convenient example.


%prep
%autosetup -n simplelist-%{version}


%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test


%files
%license LICENSE
%doc README.md
%doc simplelist.yaml
%{python3_sitelib}/*
%{_bindir}/simplelist.py


%changelog
* Fri Jul 02 2021 Andrew Williams <andy@tensixtyone.com> 0.0.2-1
- Initial RPM package
