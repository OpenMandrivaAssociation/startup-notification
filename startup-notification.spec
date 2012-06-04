%define api	1
%define major   0
%define libname	%mklibname %{name}- %{api} %{major}
%define devname	%mklibname %{name}- %{api}  -d

Summary:	Library used to monitor application startup
Name:		startup-notification
Version:	0.12
Release:	3
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
Obsoletes:	%mklibname %{name}- 1 0 -d

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
find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%{_libdir}/*-%{api}.so.%{major}*

%files -n %{devname}
%doc ChangeLog 
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

