Summary:	Display GhostScript - libraries supporting Display PostScript (DPS)
Summary(pl.UTF-8):	Display GhostScript - biblioteki wspierające Display PostScript
Name:		dgs
Version:	0.5.10
Release:	2
License:	GPL
Vendor:		The Seawood Project
Group:		X11/Libraries
Source0:	ftp://ftp.gnustep.org/pub/gnustep/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	85bf4c0be3e5325bc3bf2da3196aa299
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-time.patch
Patch2:		%{name}-am18.patch
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libwrap-devel
Requires:	ghostscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Display Ghostscript System is functionally upward-compatible with
Adobe Display PostScript, but it has been written independently. The
Display Ghostscript System provides a device-independent imaging model
for displaying information on a screen. The imaging model uses the
PostScript language which has powerful graphics capabilities and frees
the programmer from display-specific details like screen resolution
and color issues.

%description -l pl.UTF-8
Display Ghostscript System jest kompatybilny w górę pod względem
funkcjonalności z Adobe Display PostScript, został jednak napisany
niezależnie od niego. Dzięki Display Ghostscript System otrzymujemy
niezależny od urządzenia model wyświetlania informacji na ekranie.
Model ten wykorzystuje język PostScript, który posiada ogromne
możliwości graficzne i uwalnia programistę od zajmowania się
szczegółami związanymi z wyświetlaniem, takimi jak rozdzielczość
ekranu i kwestie związane z kolorami.

%package devel
Summary:	Header files etc for Display PostScript applications development
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do bibliotek do Display PostScriptu
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files etc for Display PostScript applications development.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do bibliotek do Display PostScriptu.

%package static
Summary:	Static Display PostScript libraries
Summary(pl.UTF-8):	Biblioteki statyczne DPS
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Display PostScript libraries.

%description static -l pl.UTF-8
Biblioteki statyczne DPS.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
cp -f /usr/share/automake/config.sub DPS
%configure2_13
%{__make} \
	shared=yes \
	debug=no \
	SHARE_JPEG=1 \
	gsdir=/usr/share/ghostscript/5.50 \
	gsdatadir=/usr/share/ghostscript/5.50

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	shared=yes \
	debug=no

# remove files provided by normal ghostscript
rm -rf $RPM_BUILD_ROOT%{_mandir}
(cd $RPM_BUILD_ROOT%{_bindir};
rm -f bdftops font2c gsbj gsdj gsdj500 gslj gslp gsnd printafm wftopfa
)

mv -f $RPM_BUILD_ROOT%{_datadir}/ghostscript/*/doc ./htmldoc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE FAQ NEWS README STATUS TODO ChangeLog
%attr(755,root,root) %{_bindir}/dpsexec
%attr(755,root,root) %{_bindir}/dpsnx.agent
%attr(755,root,root) %{_bindir}/makepsres
%attr(755,root,root) %{_bindir}/pswrap
%attr(755,root,root) %{_bindir}/texteroids
%attr(755,root,root) %{_bindir}/xepsf
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_datadir}/ghostscript/5.50
%{_datadir}/ghostscript/5.50/*.ps
%{_datadir}/ghostscript/5.50/Fontmap

%files devel
%defattr(644,root,root,755)
%doc htmldoc/*
%attr(755,root,root) %{_bindir}/dgs-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/DPS
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
