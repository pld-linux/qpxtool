#
# TODO:
#	- separate GUI from CLI and libs
#	- devel subpackage if useful some day
#
Summary:	CD/DVD quality checker
Summary(pl.UTF-8):	Tester jakości płyt CD/DVD
Name:		qpxtool
Version:	0.8.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/qpxtool/%{name}-%{version}.tar.bz2
# Source0-md5:	f4b09f8d5aa533f680c8bcce19c1072e
Patch0:		bad-compare.patch
Patch1:		iwyu.patch
URL:		http://qpxtool.sourceforge.net/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	qt5-build
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QPxTool gives you access to all available Quality Checks (Q-Checks) on
written and blank media, that are available for your drive. This will
help you to find the right media and the optimized writing speed for
your hardware, which will increase the chance for a long data
lifetime.

%description -l pl.UTF-8
QPxTool udostępnia wszystkie możliwe testy jakości (Q-Checks) na
zapisanym i czystym nośniku, jakie są dostępne w posiadanym napędzie.
Pomaga to odnaleźć odpowiedni nośnik i zoptymalizować prędkość zapisu
dla sprzętu, co zwiększy szanse długiego życia zapisanych danych.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
sed -e 's|lrelease|lrelease-qt5|' -i configure

%build
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--qmake=qmake-qt5 \
	%{?debug:enable-debug}
CXXFLAGS="%{rpmcxxflags}" \
CXX="%{__cxx}" \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README SupportedDevices TODO slack-desc
%attr(755,root,root) %{_bindir}/[cfqr]*
%attr(755,root,root) %{_libdir}/libq*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libq*.so.0
%attr(755,root,root) %{_libdir}/%{name}
%attr(755,root,root) %{_sbindir}/pxfw
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale
%lang(de) %{_datadir}/%{name}/locale/%{name}.de_DE.qm
%lang(ru) %{_datadir}/%{name}/locale/%{name}.ru_RU.qm
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_mandir}/man1/[cfqr]*.1*
%{_mandir}/man8/pxfw.8*
