Name:		dgs
Summary:	Display GhostScript - Libraries supporting Display PostScript (DPS)
Version:	0.5.8
Release:	1
Copyright:	GPL
Vendor:		The Seawood Project
Source:		ftp://alpha.gnu.org/gnu/gnustep/%{name}-%{version}.tar.gz
Patch:		dgs-DESTDIR.patch
Group:		Applications/Graphics
Requires:	ghostscript
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The Display Ghostscript System is functionally upward-compatible with
Adobe Display PostScript, but it has been written independently.  The
Display Ghostscript System provides a device-independent imaging model
for displaying information on a screen.  The imaging model uses the
PostScript language which has powerful graphics capabilities and frees
the programmer from display-specific details like screen resolution and
color issues.

%prep
%setup -q
%patch -p1

%build
%GNUconfigure

make shared=yes debug=no CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

make install DESTDIR=$RPM_BUILD_ROOT shared=yes debug=no

# remove files provided by normal ghostscript
rm -rf $RPM_BUILD_ROOT%{_mandir}
(cd $RPM_BUILD_ROOT%{_bindir};\
rm -f bdftops font2c gsbj gsdj gsdj500 gslj gslp gsnd printafm wftopfa)

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/* \
	$RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*.* || :

gzip -9nf ANNOUNCE FAQ NEWS README STATUS TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {ANNOUNCE,FAQ,NEWS,README,STATUS,TODO,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/*
%{_includedir}/DPS
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/lib*.so
%{_libdir}/*.a
