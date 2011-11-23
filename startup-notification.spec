%define api_version 1
%define lib_major   0
%define lib_name	%mklibname %{name}- %{api_version} %{lib_major}
%define develname	%mklibname %{name}- %{api_version}  -d

Summary: Library used to monitor application startup
Name: startup-notification
Version: 0.12
Release: 3
License: LGPLv2+
Group: System/Libraries
URL: http://www.freedesktop.org/
Source0: http://www.freedesktop.org/software/%{name}/releases/%{name}-%{version}.tar.bz2
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(x11-xcb)

%description
Startup-notification is a library used to monitor application startup.

%package -n %{lib_name}
Summary:	Library used to monitor application startup
Group:		%{group}
Provides:	lib%{name}-%{api_version} = %{version}-%{release}

%description -n %{lib_name}
Startup-notification is a library used to monitor application startup.

%package -n %{develname}
Summary:	Library used to monitor application startup
Group:		Development/C
Provides:	lib%{name}-%{api_version}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}-%{release}
Obsoletes:  %mklibname %{name}- 1 0 -d

%description -n %{develname}
Startup-notification is a library used to monitor application startup.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name '*.la' -delete

%files -n %{lib_name}
%{_libdir}/*-%{api_version}.so.%{lib_major}*

%files -n %{develname}
%doc ChangeLog 
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

