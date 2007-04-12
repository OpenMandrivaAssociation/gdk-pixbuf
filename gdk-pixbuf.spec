%define major 2
%define major_gnomecanvas 1
%define lib_name %mklibname %{name} %{major}
%define lib_canvas %mklibname %{name}-gnomecanvas %{major_gnomecanvas}
%define lib_xlib %mklibname %{name}-xlib %{major}

# define to use Xvfb
%define build_xvfb 1

# Allow --with[out] <feature> at rpm command line build
%{?_without_XVFB: %{expand: %%define build_xvfb 0}}
%{?_with_XVFB: %{expand: %%define build_xvfb 1}}

Summary:	An image loading and rendering library for Gdk
Name:		gdk-pixbuf
Version:	0.22.0
Release:	%mkrel 11
License:	LGPL
Group:		System/Libraries
BuildRequires:	gnome-libs-devel libjpeg-devel libpng-devel libtiff-devel db1-devel
BuildRequires:	libxt-devel
BuildRequires:	autoconf2.1
%if %{build_xvfb}
BuildRequires:	XFree86-Xvfb
%endif
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
BuildRoot:	%{_tmppath}//%{name}-%{version}-%{release}-buildroot
URL:		http://www.gnome.org/
Requires:	%{name}-loaders = %{version}

%description
The GdkPixBuf library provides a number of features:
 - Image loading facilities.
 - Rendering of a GdkPixBuf into various formats:
   drawables (windows, pixmaps), GdkRGB buffers.

%package -n	%{lib_name}
Summary:	An image loading and rendering library for Gdk
Group:		System/Libraries
Requires:	%{name}-loaders = %{version}
Obsoletes:	gdk-pixbuf
Provides:	gdk-pixbuf = %{version}

%description -n	%{lib_name}
The GdkPixBuf library provides a number of features:
 - Image loading facilities.
 - Rendering of a GdkPixBuf into various formats:
   drawables (windows, pixmaps), GdkRGB buffers.

This package provides GTK+ version of gdk-pixbuf

%package -n	%{lib_canvas}
Summary:	An image loading and rendering library for Gdk
Group:		System/Libraries
Requires:	gnome-libs %{name}-loaders = %{version}
Obsoletes:	%{name}-gnomecanvas
Provides:	%{name}-gnomecanvas = %{version}
Obsoletes:	lib%{name}-gnomecanvas2 <= 0.13.0-1mdk
Provides:	lib%{name}-gnomecanvas2 = %{version}

%description -n	%{lib_canvas}
The GdkPixBuf library provides a number of features:
 - Image loading facilities.
 - Rendering of a GdkPixBuf into various formats:
   drawables (windows, pixmaps), GdkRGB buffers.

This package provides GNOME version of gdk-pixbuf

%package -n	%{lib_xlib}
Summary:	An image loading and rendering library for Gdk
Group:		System/Libraries
Requires:	%{name}-loaders = %{version}
Obsoletes:	%{name}-xlib
Provides:	%{name}-xlib = %{version}

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
Requires:	%{lib_canvas} = %{version}
Requires:	%{lib_xlib} = %{version}
Requires:	%{lib_name} = %{version}
Obsoletes:	%{name}-devel
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}

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

# needed by patches 1 & 4
WANT_AUTOCONF_2_1=1 autoconf

%build
%configure2_5x --disable-gtk-doc

%if %{build_xvfb}
XDISPLAY=$(i=0; while [ -f /tmp/.X$i-lock ]; do i=$(($i+1)); done; echo $i)
Xvfb :$XDISPLAY >& /dev/null &
DISPLAY=:$XDISPLAY %make
kill $(cat /tmp/.X$XDISPLAY-lock)
%else
%make
%endif


%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/gdk-pixbuf-config

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%post -n %{lib_xlib} -p /sbin/ldconfig

%postun -n %{lib_xlib} -p /sbin/ldconfig

%post -n %{lib_canvas} -p /sbin/ldconfig

%postun -n %{lib_canvas} -p /sbin/ldconfig

%post loaders -p /sbin/ldconfig

%postun loaders -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.LIB NEWS README TODO 
%{_libdir}/libgdk_pixbuf.so.*

%files loaders
%defattr(-,root,root)
%dir %{_libdir}/gdk-pixbuf
%dir %{_libdir}/gdk-pixbuf/loaders
%{_libdir}/gdk-pixbuf/loaders/*.so*

%files -n %{lib_xlib} 
%defattr(-,root,root)
%{_libdir}/*xlib.so.*

%files -n %{lib_canvas}
%defattr(-,root,root)
%{_libdir}/*gnomecanvas*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%{_bindir}/*-config
%multiarch %{multiarch_bindir}/*-config
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/libgdk*.so
%{_libdir}/libgnome*.so
%{_libdir}/gdk-pixbuf/loaders/*a
%{_includedir}/*
%{_datadir}/aclocal/*
%{_libdir}/*.sh
%{_datadir}/gnome/html/*


