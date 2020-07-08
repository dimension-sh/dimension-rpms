# Fedora review: http://bugzilla.redhat.com/249365

# crasher workaround, http://bugzilla.redhat.com/1282092
%undefine _hardened_build

Summary: powerful, easy to use console email client
Name: alpine-maildir
Version: 2.22
Release: 2%{?dist}

License: ASL 2.0
URL:     http://alpine.x10host.com/
Source0: http://alpine.x10host.com/alpine/patches/alpine-%{version}/alpine-%{version}.tar.xz
Source1: README.fedora

Patch1: alpine-2.21-useragent.patch
Patch2: alpine-2.21-gcc10.patch
Patch3: alpine-2.22-maildir.patch

# Using "Conflicts" instead of Obsoletes because while alpine is substantially
# compatible with pine the change to Unicode breaks important user
# functionality such as non-ASCII encoded saved passwords. Additionally, there
# are also many patches to pine floating around that for political/technical
# reasons will not be integrated into alpine. (I'd like to stay out of it...
# just search "Mark Crispin maildir" for the gory details.) Since licensing
# prevents a Fedora pine package, I cannot predict what patches users might
# have and so want to warn them instead of automatically replacing their pine
# install with an alpine that could break their configuration. 
# I understand this to be a special case of the "Optional Functionality"
# description at http://fedoraproject.org/wiki/Packaging/Conflicts
Conflicts: pine, alpine

Provides: re-alpine = %{version}-%{release}

#BuildRequires: automake libtool
BuildRequires: gettext
BuildRequires: hunspell
## passing --with-npa=/usr/bin/inews
#BuildRequires: inews
BuildRequires: krb5-devel
BuildRequires: ncurses-devel 
BuildRequires: openldap-devel
BuildRequires: openssl-devel
BuildRequires: pam-devel
BuildRequires: passwd
# passing --with-smtp-msa=/usr/sbin/sendmail instead
#BuildRequires: /usr/sbin/sendmail 

Requires: hunspell
Requires: mailcap
Requires: /usr/sbin/sendmail

BuildRequires: gcc

%description
Alpine -- an Alternatively Licensed Program for Internet
News & Email -- is a tool for reading, sending, and managing
electronic messages.  Alpine is the successor to Pine and was
developed by Computing & Communications at the University of
Washington.  
  Though originally designed for inexperienced email users,
Alpine supports many advanced features, and an ever-growing number of
configuration and personal-preference options.
Changes and enhancements over pine:
  * Released under the Apache Software License, Version 2.0.
  * Internationalization built around new internal Unicode support.
  * Ground-up reorganization of source code around new "pith/" core 
routine library.
  * Ground-up reorganization of build and install procedure based on 
GNU Build System's autotools.


%prep
%setup -q -n alpine-%{version}
%patch1 -p1
%patch2 -p1

install -m644 -p %{SOURCE1} .


%build
touch imap/ip6
# --without-tcl disables the TCL-based CGI "Web Alpine"
%configure \
  --enable-debug=no \
  --without-tcl \
  --with-c-client-target=lfd \
  --with-smtp-msa=/usr/sbin/sendmail \
  --with-npa=/usr/bin/inews \
  --with-passfile=.alpine.passfile \
  --with-simple-spellcheck=hunspell \
  --with-interactive-spellcheck=hunspell \
  --with-system-pinerc=%{_sysconfdir}/pine.conf \
  --with-system-fixed-pinerc=%{_sysconfdir}/pine.conf.fixed

%make_build EXTRACFLAGS="$RPM_OPT_FLAGS"


%install
%make_install

# create/touch %ghost'd files
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
touch $RPM_BUILD_ROOT%{_sysconfdir}/pine.conf
touch $RPM_BUILD_ROOT%{_sysconfdir}/pine.conf.fixed


%files
%doc README
%doc README.fedora
%license LICENSE
%ghost %config(noreplace) %{_sysconfdir}/pine.conf
%ghost %config(noreplace) %{_sysconfdir}/pine.conf.fixed
%{_bindir}/alpine
%{_bindir}/pico
%{_bindir}/pilot
%{_bindir}/rpload
%{_bindir}/rpdump
%{_mandir}/man1/alpine.1*
%{_mandir}/man1/pico.1*
%{_mandir}/man1/pilot.1*
%{_mandir}/man1/rpload.1*
%{_mandir}/man1/rpdump.1*


%changelog
* Wed Jul 08 2020 Andrew Williams <andy@tensixtyone.com - 2.22-2
- Renamed to 'alpine-maildir' and applyed maildir.patch
* Fri May 29 2020 Paul Wouters <pwouters@redhat.com> - 2.22-1
- Resolves: rhbz#1830335 Add alpine branch to EPEL 8
- Imported from rawhide fedora package
