%global _hardened_build 1
%define _unpackaged_files_terminate_build 0

Summary: lowdown is a Markdown translator producing HTML5, roff documents in the ms and man formats, LaTeX, gemini, and terminal output.
Name: lowdown
Version: 0.10.0
Release: 1%{?dist}
License: ISC License
Group: Applications/Internet

Source0: https://github.com/kristapsdz/lowdown/archive/refs/tags/VERSION_0_10_0.tar.gz#/lowdown-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: glibc-devel

%description
lowdown is a Markdown translator producing HTML5, roff documents in the ms and man formats, LaTeX, gemini, and terminal output.

%prep

%setup -n lowdown-VERSION_0_10_0

%build
echo -e "PREFIX=%{_prefix}\nMANDIR=%{_mandir}\nINSTALL_PROGRAM=\"install -m 0755\"\nINSTALL_LIB=\"install -m 0755\"\nINSTALL_MAN=\"install -m 0644\"\nINSTALL_DATA=\"install -m 0644\"\n" > configure.local
./configure
make %{?_smp_mflags} all

%install
DESTDIR=%{buildroot} PREFIX=%{_prefix} MANDIR=%{_mandir} make install

%clean
rm -rf %{buildroot}

%post

%preun

%postun

%files
%doc README.md
%license LICENSE.md
%attr(0755,root,root) %{_bindir}/lowdown*
%{_mandir}/*/*
