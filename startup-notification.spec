%define api_version 1
%define lib_major   0
%define lib_name	%mklibname %{name}- %{api_version} %{lib_major}
%define develname %mklibname %{name}- %{api_version}  -d

Summary: Library used to monitor application startup
Name: startup-notification
Version: 0.9
Release: %mkrel 3
License: LGPL
Group: System/Libraries
URL: http://www.freedesktop.org/
Source0: http://www.freedesktop.org/software/%name/releases/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: X11-devel

%description
Startup-notification is a library used to monitor application startup.

%package -n %{lib_name}
Summary:	Library used to monitor application startup
Group:		%{group}
Provides:	lib%{name}-%{api_version} = %{version}-%{release}

%description -n %{lib_name}
Startup-notification is a library used to monitor application startup.

%package -n %develname
Summary:	Library used to monitor application startup
Group:		Development/C
Provides:	lib%{name}-%{api_version}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}-%{release}
Obsoletes:  %mklibname %{name}- 1 0 -d

%description -n %develname
Startup-notification is a library used to monitor application startup.

%prep
%setup -q

%build
%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig -n %{lib_name}

%postun -p /sbin/ldconfig -n %{lib_name}

%files -n %{lib_name}
%defattr(-,root,root,-)
%doc ChangeLog 
%{_libdir}/*.so.*

%files -n %develname
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*


