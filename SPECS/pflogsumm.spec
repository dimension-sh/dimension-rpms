%global _hardened_build 1

Summary: A Postfix log processor
Name: pflogsumm
Version: 1.1.5
Release: 1%{?dist}
License: GPL
Group: Applications/Internet

Source0: https://jimsun.linxnet.com/downloads/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: perl
Requires: perl-Date-Calc

%description
pflogsumm.pl is designed to provide an over-view of postfix activity, with just enough detail to give the administrator a "heads up" for potential trouble spots. 

%prep

%setup

%build

%install
install -D -m 0755 pflogsumm.pl $RPM_BUILD_ROOT%{_bindir}/pflogsumm
install -D -m 0755 pflogsumm.1 $RPM_BUILD_ROOT%{_mandir}/man1/pflogsumm.1
install -D -t $RPM_BUILD_ROOT%{_docdir}/pflogsumm/ ChangeLog pflogsumm-faq.txt README ToDo
%clean
rm -rf %{buildroot}

%post

%preun

%postun

%files
%attr(0755,root,root) %{_bindir}/pflogsumm
%doc %{_mandir}/man1/*
%doc ChangeLog pflogsumm-faq.txt README ToDo

%changelog
* Tue Jun 09 2021 Andrew Williams <andy@tensixtyone.com> 1.1.5-1
- Initial RPM package
