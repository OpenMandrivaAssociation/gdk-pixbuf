%define major 2
%define major_gnomecanvas 1
%define lib_name %mklibname %{name} %{major}
%define lib_canvas %mklibname %{name}-gnomecanvas %{major_gnomecanvas}
%define lib_xlib %mklibname %{name}-xlib %{major}

# define to use Xvfb
%define build_xvfb 0

# Allow --with[out] <feature> at rpm command line build
%{?_without_XVFB: %{expand: %%define build_xvfb 0}}
%{?_with_XVFB: %{expand: %%define build_xvfb 1}}

Summary:	An image loading and rendering library for Gdk
Name:		gdk-pixbuf
Version:	0.22.0
Release:	19
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/unstable/%{name}/%{name}-%{version}.tar.bz2
Patch0:		gdk-pixbuf-demolink.patch
# (fc) 0.18.0-1mdk don't add -Llibdir to gdk-pixbuf-config --libs
Patch1:		gdk-pixbuf-0.18.0-libdir.patch
# (fc) 0.22.0-4mdk security update for CAN-2004-0782, CAN-2004-0783, CAN-2004-0788, and CAN-2004-0753
Patch2:		gdk-pixbuf-0.22.0-CAN-2004-0753.patch
Patch3:		gdk-pixbuf-0.22.0-loaders.patch
# (gb) 0.22.0-7mdk this applies to aclocal.m4 directly, don't bother with older aclocal
Patch4:		gdk-pixbuf-0.22.0-libtool.patch
# (fc) 0.22.0-8mdk fix BMP vulnerability (CVS) (CAN-2005-0891)
Patch5:		gdk-pixbuf-0.22.0-bmpcrash.patch
# (fc) 0.22.0-8mdk fix ICO width (Fedora)
Patch6:		gdk-pixbuf-0.22.0-ico-width.patch
Patch7:		gdk-pixbuf-0.22.0-fix-underquoted-calls.patch
Patch8:		gdk-pixbuf-0.22.0-rgb.txt_fix.diff
Patch9:		gdk-pixbuf-0.22.0-linkage_fix.diff
Patch10:	gdk-pixbuf-0.22.0-remove-gmodule-configure-check.patch
Patch11:	gdk-pixbuf-0.22.0-automake.patch
Patch12:	gdk-pixbuf-0.22.0-libpng15.patch
Patch13:	gdk-pixbuf-0.22.0-automake-1.13.patch
Requires:	%{name}-loaders = %{version}-%{release}
BuildRequires:	db1-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	tiff-devel
BuildRequires:	automake
BuildRequires:	pkgconfig(xt)
BuildRequires:	rgb
%if %{build_xvfb}
BuildRequires:	XFree86-Xvfb
%endif

%description
The GdkPixBuf library provides a number of features:
 - Image loading facilities.
 - Rendering of a GdkPixBuf into various formats:
   drawables (windows, pixmaps), GdkRGB buffers.

%package -n	%{lib_name}
Summary:	An image loading and rendering library for Gdk
Group:		System/Libraries
Requires:	%{name}-loaders = %{version}-%{release}
Provides:	gdk-pixbuf = %{version}-%{release}

%description -n	%{lib_name}
The GdkPixBuf library provides a number of features:
 - Image loading facilities.
 - Rendering of a GdkPixBuf into various formats:
   drawables (windows, pixmaps), GdkRGB buffers.

This package provides GTK+ version of gdk-pixbuf

%package -n	%{lib_canvas}
Summary:	An image loading and rendering library for Gdk
Group:		System/Libraries
Requires:	%{name}-loaders = %{version}-%{release}
Provides:	%{name}-gnomecanvas = %{version}-%{release}
Provides:	lib%{name}-gnomecanvas2 = %{version}-%{release}

%description -n	%{lib_canvas}
The GdkPixBuf library provides a number of features:
 - Image loading facilities.
 - Rendering of a GdkPixBuf into various formats:
   drawables (windows, pixmaps), GdkRGB buffers.

This package provides GNOME version of gdk-pixbuf

%package -n	%{lib_xlib}
Summary:	An image loading and rendering library for Gdk
Group:		System/Libraries
Requires:	%{name}-loaders = %{version}-%{release}
Provides:	%{name}-xlib = %{version}-%{release}

%description -n	%{lib_xlib}
The GdkPixBuf library provides a number of features:
 - Image loading facilities.
 - Rendering of a GdkPixBuf into various formats:
   drawables (windows, pixmaps), GdkRGB buffers.

This package provides Xlib version of gdk-pixbuf

%package	loaders
Summary:	An image loading and rendering library for Gdk
Group:		System/Libraries

%description	loaders
The GdkPixBuf library provides a number of features:
 - Image loading facilities.
 - Rendering of a GdkPixBuf into various formats:
   drawables (windows, pixmaps), GdkRGB buffers.

This package provides image loaders used by all versions
of GdkPixBuf

%package -n	%{lib_name}-devel
Summary:	Development tools for GdkPixBuf applications
Group:		Development/GNOME and GTK+
Requires:	%{lib_canvas} = %{version}-%{release}
Requires:	%{lib_xlib} = %{version}-%{release}
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{lib_name}-devel
The header files, static libraries and documentation needed for
deeveloping GdkPixBuf applications. GdkPixBuf is an image loading and rendering
library for Gdk.

Install the imlib-devel package if you want to develop Imlib applications.
You'll also need to install the gdk-pixbuf package.

%prep
%setup -q
%patch0 -p1 -b .demolink
%patch1 -p1 -b .libdir
%patch2 -p1 -b .can-2004-0753
%patch3 -p1 -b .can-2004-0782_0783_0788
%patch4 -p1 -b .libtool
%patch5 -p1 -b .bmpcrash
%patch6 -p1 -b .ico-width
%patch7 -p1 -b .underquoted
%patch8 -p0
%patch9 -p1
%patch10 -p0
%patch11 -p0
%patch12 -p1 -b .libpng15
%patch13 -p1 -b .am113~

# Converting NEWS to UTF-8
iconv -f iso8859-1 -t utf-8 NEWS > NEWS.conv && mv -f NEWS.conv NEWS

# needed by patches 1 & 4
libtoolize --install --force
aclocal
autoconf
automake -a -c

%build
%define _disable_ld_no_undefined 1
%configure2_5x --disable-gtk-doc

%if %{build_xvfb}
XDISPLAY=$(i=0; while [ -f /tmp/.X$i-lock ]; do i=$(($i+1)); done; echo $i)
Xvfb :$XDISPLAY >& /dev/null &
DISPLAY=:$XDISPLAY make
kill $(cat /tmp/.X$XDISPLAY-lock)
%else
make
%endif


%install
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/gdk-pixbuf-config

%files -n %{lib_name}
%doc AUTHORS COPYING COPYING.LIB NEWS README TODO
%{_libdir}/libgdk_pixbuf.so.*

%files loaders
%dir %{_libdir}/gdk-pixbuf
%dir %{_libdir}/gdk-pixbuf/loaders
%{_libdir}/gdk-pixbuf/loaders/*.so*

%files -n %{lib_xlib}
%{_libdir}/*xlib.so.*

%files -n %{lib_canvas}
%{_libdir}/*gnomecanvas*.so.*

%files -n %{lib_name}-devel
%{_bindir}/*-config
%multiarch %{multiarch_bindir}/*-config

%{_libdir}/*.a
%{_libdir}/libgdk*.so
%{_libdir}/libgnome*.so
%{_libdir}/gdk-pixbuf/loaders/*a
%{_includedir}/*
%{_datadir}/aclocal/*
%{_libdir}/*.sh
%{_datadir}/gnome/html/*


%changelog
* Sat Mar 17 2012 Andrew Lukoshko <andrew.lukoshko@rosalab.ru> 0.22.0-18mdv2011.0
- fixed build with actual automake
- fixed explicit-lib-dependency
- fixed self-obsoletion
- fixed non-utf8 NEWS

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.22.0-17mdv2011.0
+ Revision: 610821
- rebuild

* Mon Jan 11 2010 Funda Wang <fwang@mandriva.org> 0.22.0-16mdv2010.1
+ Revision: 489456
- rebuild for libjpegv8

* Mon Aug 17 2009 Götz Waschk <waschk@mandriva.org> 0.22.0-15mdv2010.0
+ Revision: 417153
- add more build hacks
- update license
- build with system libtool

* Wed Jul 30 2008 Oden Eriksson <oeriksson@mandriva.com> 0.22.0-14mdv2009.0
+ Revision: 255526
- fix build (libtool mess...)
- fix linkage
- disable parallel build
- disable the Xvfb stuff
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Thu Mar 01 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.22.0-11mdv2007.0
+ Revision: 130698
- Import gdk-pixbuf

* Thu Mar 01 2007 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.22.0-11mdv2007.1
- don't package big ChangeLog

* Thu Aug 10 2006 Götz Waschk <waschk@mandriva.org> 0.22.0-10mdv2007.0
- fix buildrequires

* Tue Jan 31 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.22.0-9mdk
- fix underquoted calls (P7)
- %%mkrel

* Fri Apr 08 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.22.0-8mdk
- Patch5 (CVS): fix BMP vulnerability (CVS) (CAN-2005-0891)
- Patch6 (Fedora): fix ico width

* Wed Feb 09 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.22.0-7mdk
- old libtool fixes

* Tue Feb 01 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.22.0-6mdk
- Disable doc generation
- multiarch
- Remove explicit requires
- fix rpmlint error/warnings

* Tue Sep 21 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.22.0-5mdk
- Update patch3 to fix error from gtk hackers
- Fix build on x86-64

* Fri Sep 17 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.22.0-4mdk
- Patches 2 & 3 : security update for CAN-2004-0782, CAN-2004-0783,
  CAN-2004-0788, and CAN-2004-0753

* Wed Jun 09 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.22.0-3mdk
- fix buildrequires
- cosmetics
