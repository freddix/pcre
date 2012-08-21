Summary:	Perl-Compatible Regular Expression library
Name:		pcre
Version:	8.31
Release:	1
License:	BSD (see LICENCE)
Group:		Libraries
Source0:	ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/%{name}-%{version}.tar.bz2
# Source0-md5:	1c9a276af932b5599157f96e945391f0
URL:		http://www.pcre.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PCRE stands for the Perl Compatible Regular Expression library. It
contains routines to match text against regular expressions similar to
Perl's. It also contains a POSIX compatibility library.

%package devel
Summary:	Perl-Compatible Regular Expression header files and development documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Perl-Compatible Regular Expression header files and development
documentation.

%package cxx
Summary:	C++ wrapper to PCRE library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description cxx
C++ wrapper to PCRE library.

%package cxx-devel
Summary:	Header file for C++ wrapper to PCRE library
Group:		Development/Libraries
Requires:	%{name}-cxx = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description cxx-devel
Header file for C++ wrapper to PCRE library.

%package -n pcregrep
Summary:	Grep using Perl Compatible Regular Expressions
Group:		Applications/Text
Obsoletes:	pgrep

%description -n pcregrep
pgrep is a grep workalike which uses perl-style regular expressions
instead of POSIX regular expressions.

%package -n pcretest
Summary:	A program for testing Perl-comaptible regular expressions
Group:		Applications/Text

%description -n pcretest
pcretest is a program which you can use to test regular expression

%package doc-html
Summary:	Documentation for PCRE in HTML format
Group:		Applications/Text

%description doc-html
Documentation for PCRE in HTML format.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	CXXLDFLAGS="%{rpmldflags}"	\
	--enable-jit			\
	--enable-pcre16			\
	--enable-static=no		\
	--enable-unicode-properties	\
	--enable-utf8
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/pcre

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   cxx -p /sbin/ldconfig
%postun cxx -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS LICENCE
%attr(755,root,root) %ghost %{_libdir}/libpcre.so.?
%attr(755,root,root) %ghost %{_libdir}/libpcre16.so.?
%attr(755,root,root) %ghost %{_libdir}/libpcreposix.so.?
%attr(755,root,root) %{_libdir}/libpcre.so.*.*.*
%attr(755,root,root) %{_libdir}/libpcre16.so.*.*.*
%attr(755,root,root) %{_libdir}/libpcreposix.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcre-config
%attr(755,root,root) %{_libdir}/libpcre.so
%attr(755,root,root) %{_libdir}/libpcre16.so
%attr(755,root,root) %{_libdir}/libpcreposix.so
%{_libdir}/libpcre.la
%{_libdir}/libpcre16.la
%{_libdir}/libpcreposix.la
%{_includedir}/pcre.h
%{_includedir}/pcreposix.h
%{_pkgconfigdir}/libpcre.pc
%{_pkgconfigdir}/libpcre16.pc
%{_pkgconfigdir}/libpcreposix.pc
%{_mandir}/man1/pcre-config.1*
%{_mandir}/man3/*
%exclude %{_mandir}/man3/pcrecpp.3*

%files cxx
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libpcrecpp.so.?
%attr(755,root,root) %{_libdir}/libpcrecpp.so.*.*.*

%files cxx-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcrecpp.so
%{_libdir}/libpcrecpp.la
%{_includedir}/pcrecpp.h
%{_includedir}/pcre_scanner.h
%{_includedir}/pcre_stringpiece.h
%{_includedir}/pcrecpparg.h
%{_mandir}/man3/pcrecpp.3*
%{_pkgconfigdir}/libpcrecpp.pc

%files -n pcregrep
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcregrep
%{_mandir}/man1/pcregrep.1*

%files -n pcretest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcretest
%{_mandir}/man1/pcretest.1*

%files doc-html
%defattr(644,root,root,755)
%doc doc/html/*

