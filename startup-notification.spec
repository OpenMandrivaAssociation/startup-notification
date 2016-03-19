%define api	1
%define major	0
%define libname	%mklibname %{name}- %{api} %{major}
%define devname	%mklibname %{name}- %{api}  -d

Summary:	Library used to monitor application startup
Name:		startup-notification
Version:	0.12
Release:	18
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.freedesktop.org/
Source0:	http://www.freedesktop.org/software/%{name}/releases/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(x11-xcb)

%description
Startup-notification is a library used to monitor application startup.

%package -n %{libname}
Summary:	Library used to monitor application startup
Group:		%{group}
Provides:	lib%{name}-%{api} = %{version}-%{release}

%description -n %{libname}
Startup-notification is a library used to monitor application startup.

%package -n %{devname}
Summary:	Library used to monitor application startup
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname startup-notification- 1 0 -d} < 0.12-5

%description -n %{devname}
Startup-notification is a library used to monitor application startup.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*-%{api}.so.%{major}*

%files -n %{devname}
%doc ChangeLog
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
* Mon Jun 04 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.12-4
+ Revision: 802431
- rebuild for new xcb-util

* Wed Nov 23 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.12-3
+ Revision: 732795
- adjusted BR
- rebuild
- cleaned up spec
- removed defattr
- removed .la files
- disabled static build
- removed old ldconfig scriptlets
- removed clean section
- converted BRs to pkgconfig provides
- remove mkrel & BuildRoot

* Tue Oct 11 2011 Rafael da Veiga Cabral <cabral@mandriva.com> 0.12-2
+ Revision: 704138
+ rebuild (emptylog)

* Sat May 21 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.12-1
+ Revision: 676597
- update to new version 0.12

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10-6
+ Revision: 670202
- mass rebuild

* Wed Dec 15 2010 Funda Wang <fwang@mandriva.org> 0.10-5mdv2011.0
+ Revision: 621895
- rebuild for BS monster

* Wed Dec 15 2010 Funda Wang <fwang@mandriva.org> 0.10-4mdv2011.0
+ Revision: 621884
- reduce BR

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10-3mdv2011.0
+ Revision: 607752
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10-2mdv2010.1
+ Revision: 524135
- rebuilt for 2010.1

* Mon May 04 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.10-1mdv2010.0
+ Revision: 371622
- update build deps
- update license
- update to new version 0.10

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.9-7mdv2009.0
+ Revision: 225478
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9-6mdv2008.1
+ Revision: 179532
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 02 2007 Andreas Hasenack <andreas@mandriva.com> 0.9-5mdv2008.0
+ Revision: 47113
- fix wrong obsoletes (#31644)

* Wed Jun 27 2007 Andreas Hasenack <andreas@mandriva.com> 0.9-4mdv2008.0
+ Revision: 45151
- rebuild (-devel got lost somehow)

* Tue Jun 26 2007 Thierry Vignaud <tv@mandriva.org> 0.9-3mdv2008.0
+ Revision: 44462
- update buildrequires to new xorg

* Fri Jun 22 2007 Thierry Vignaud <tv@mandriva.org> 0.9-2mdv2008.0
+ Revision: 43087
- new devel library policy


* Sat Apr 07 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.9-1mdv2007.1
+ Revision: 150956
- new version
- Import startup-notification

* Wed Sep 13 2006 Frederic Crozat <fcrozat@mandriva.com> 0.8-3mdv2007.0
- Rebuild

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.8-2mdk
- Rebuild

* Thu Dec 02 2004 Götz Waschk <waschk@linux-mandrake.com> 0.8-1mdk
- new source URL
- New release 0.8

* Fri Jun 25 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7-1mdk
- fix source url
- reenable libtoolize
- New release 0.7

