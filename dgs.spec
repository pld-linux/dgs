Name:		dgs
Summary:	Display GhostScript - Libraries supporting Display PostScript (DPS)
Version:	0.5.0
Release:	1
Copyright:	GPL
Vendor:		The Seawood Project
Source:		ftp://alpha.gnu.org/gnu/gnustep/%{name}-%{version}.tar.gz
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
%setup -n dgs

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
CXXFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
	--prefix=/usr

make shared=yes debug=no

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr

make install prefix=$RPM_BUILD_ROOT/usr shared=yes debug=no

# remove files provided by normal ghostscript
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd $RPM_BUILD_ROOT%{_bindir}
rm bdftops font2c gsbj gsdj gsdj500 gslj gslp gsnd pdf2dsc pdf2ps printafm \
   ps2ascii ps2epsi ps2pdf wftopfa

%files
%doc ANNOUNCE FAQ INSTALL NEWS README STATUS SUPPORT TODO
%{_bindir}/*
%{_includedir}/DPS
%{_libdir}/DGS
%{_libdir}/*.a

%changelog
* Fri Feb  5 1999 Bernhard Rosenkraenzer <bero@microsoft.sucks.eu.org>
- initial RPM
