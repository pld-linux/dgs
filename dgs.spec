Summary:	Display GhostScript - Libraries supporting Display PostScript (DPS)
Summary(pl):	Display GhostScript - biblioteki wspieraj±ce Display PostScript
Name:		dgs
Version:	0.5.10
Release:	1
License:	GPL
Vendor:		The Seawood Project
Group:		X11/Libraries
Source0:	ftp://ftp.gnustep.org/pub/gnustep/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	85bf4c0be3e5325bc3bf2da3196aa299
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-time.patch
BuildRequires:	XFree86-devel
BuildRequires:	glib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libwrap-devel
Requires:	ghostscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_aclocaldir	%(aclocal --print-ac-dir)

%description
The Display Ghostscript System is functionally upward-compatible with
Adobe Display PostScript, but it has been written independently. The
Display Ghostscript System provides a device-independent imaging model
for displaying information on a screen. The imaging model uses the
PostScript language which has powerful graphics capabilities and frees
the programmer from display-specific details like screen resolution
and color issues.

%description -l pl
Display Ghostscript System jest kompatybilny w górê pod wzglêdem
funkcjonalno¶ci z Adobe Display PostScript, zosta³ jednak napisany
niezale¿nie od niego. Dziêki Display Ghostscript System otrzymujemy
niezale¿ny od urz±dzenia model wyswietlania informacji na ekranie.
Model ten wykorzystuje jêzyk PostScript, który posiada ogromne
mozliwo¶ci graficzne i uwalnia programistê od zajmowania siê
szczegó³ami zwi±zanymi z wy¶wietlaniem, takimi jak rozdzielczo¶æ
ekranu i kwestie zwi±zane z kolorami.

%package devel
Summary:	Header files and etc for develop Display PostScript applications
Summary(pl):	Pliki nag³ówkowe i dokumentacja do bibliotek do Display PostScriptu
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and etc for develop Display PostScript applications.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do bibliotek do Display PostScriptu.

%package static
Summary:	Static Display PostScript libraries
Summary(pl):	Biblioteki statyczne DPS
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Display PostScript libraries.

%description static -l pl
Biblioteki statyczne DPS.

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
%configure2_13
%{__make} \
	shared=yes \
	debug=no \
	SHARE_JPEG=1 \
	gsdir=/usr/share/ghostscript \
	gsdatadir=/usr/share/ghostscript \

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	shared=yes debug=no

# remove files provided by normal ghostscript
rm -rf $RPM_BUILD_ROOT%{_mandir}
(cd $RPM_BUILD_ROOT%{_bindir};
rm -f bdftops font2c gsbj gsdj gsdj500 gslj gslp gsnd printafm wftopfa
)

mv -f $RPM_BUILD_ROOT%{_datadir}/ghostscript/*/doc ./htmldoc

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
