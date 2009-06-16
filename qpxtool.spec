#
# TODO:
#	- devel subpackage if useful some day
#
Summary:	CD/DVD quality checker
Summary(pl.UTF-8):	Tester jakości płyt CD/DVD
Name:		qpxtool
Version:	0.6.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qpxtool/%{name}-%{version}.tar.bz2
# Source0-md5:	4fa7ce8aa9c13aa2db0a8b5224acb906
Patch0:		%{name}-llh.patch
Patch1:		%{name}-0.6.1-libata.txt
URL:		http://qpxtool.sourceforge.net/
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QPxTool gives you access to all available Quality Checks (Q-Checks) on
written and blank media, that are available for your drive. This will
help you to find the right media and the optimized writing speed for
your hardware, which will increase the chance for a long data lifetime.

%description -l pl.UTF-8
QPxTool udostępnia wszystkie możliwe testy jakości (Q-Checks) na
zapisanym i czystym nośniku, jakie są dostępne w posiadanym napędzie.
Pomaga to odnaleźć odpowiedni nośnik i zoptymalizować prędkość zapisu
dla sprzętu, co zwiększy szanse długiego życia zapisanych danych.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
export QTDIR="%{_prefix}"
export QMAKESPEC="linux-g++"
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX="%{_prefix}" \
	MANDIR="%{_mandir}" \
	QTDIR="%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO slack-desc
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man8/*.8*
