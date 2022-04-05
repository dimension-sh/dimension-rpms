%global _hardened_build 1

Summary: NNCP (Node to Node copy) is a collection of utilities simplifying secure store-and-forward files, mail and command exchanging.
Name: nncp
Version: 8.7.2
Release: 1%{?dist}
License: GNU GPL v3
Group: Applications/Internet

Source0: http://www.nncpgo.org/download/nncp-%{version}.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
NNCP (Node to Node copy) is a collection of utilities simplifying secure store-and-forward files, mail and command exchanging.

%prep

%setup

%build

%install
GO_LDFLAGS="-linkmode=external" INFODIR=%{buildroot}%{_infodir} LOGPATH=%{_localstatedir}/log/nncp DESTDIR=%{buildroot} PREFIX=%{_prefix} MANDIR=%{_mandir} make install
mkdir -p %{buildroot}%{_localstatedir}/log/nncp
mkdir -p %{buildroot}%{_localstatedir}/spool/nncp

%clean
rm -rf %{buildroot}

%post

%preun

%postun

%files
%doc AUTHORS
%doc README
%doc README.RU
%doc NEWS
%doc NEWS.RU
%doc THANKS
%attr(0644,root,root) %{_infodir}/nncp.info.gz
%license COPYING
%attr(0755,root,root) %{_bindir}/nncp-*
%dir %{_localstatedir}/spool/nncp
%dir %{_localstatedir}/log/nncp
