Name: dgs
Summary: Display GhostScript - Libraries supporting Display PostScript (DPS)
Version: 0.5.0
Release: bero1
Copyright: Free Software
Source: dgs.tar.bz2
Source1: jpeg.tar.bz2
Source2: zlib.tar.bz2
Source3: png.tar.bz2
Group: Applications/Graphics
Requires: ghostscript
BuildRoot: /var/tmp/dgs-root

%description
The Display Ghostscript System is functionally upward-compatible with
Adobe Display PostScript, but it has been written independently.  The
Display Ghostscript System provides a device-independent imaging model
for displaying information on a screen.  The imaging model uses the
PostScript language which has powerful graphics capabilities and frees
the programmer from display-specific details like screen resolution and
color issues.

%prep
%setup -n dgs -a 1 -a 2 -a 3
mv jpeg gs/jpeg-6a
mv zlib gs
mv png gs/libpng
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr

%build
make shared=yes debug=no

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
make install prefix=$RPM_BUILD_ROOT/usr shared=yes debug=no

# remove files provided by normal ghostscript
rm -rf $RPM_BUILD_ROOT/usr/man
cd $RPM_BUILD_ROOT/usr/bin
rm bdftops font2c gsbj gsdj gsdj500 gslj gslp gsnd pdf2dsc pdf2ps printafm \
   ps2ascii ps2epsi ps2pdf wftopfa

%files
%doc ANNOUNCE FAQ INSTALL NEWS README STATUS SUPPORT TODO
/usr/bin/*
/usr/include/DPS
/usr/lib/DGS
/usr/lib/*.a

%changelog
* Fri Feb  5 1999 Bernhard Rosenkraenzer <bero@microsoft.sucks.eu.org>
- initial RPM
