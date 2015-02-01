Summary:   A hash table for C structures
Name:      uthash
Version:   1.9.3
Release:   1
License:   BSD-style single-clause
Group:     System/Kernel
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source0:   %{name}-%{version}.tar.bz2

%description
Any C structure can be stored in a hash table using 
uthash. Just add a UT_hash_handle to the structure 
and choose one or more fields in your structure to 
act as the key. Then use these macros to store, 
retrieve or delete items from the hash table.

%package devel
Summary: %{summary}
Group: Development/Libraries

%description devel
Description: %{summary}

%prep
%setup -q 
%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p  $RPM_BUILD_ROOT/usr/include
cd src
cp utarray.h uthash.h utlist.h utstring.h $RPM_BUILD_ROOT/usr/include


%clean

%files devel
%defattr(-,root,root,-)
%{_includedir}/utarray.h
%{_includedir}/uthash.h
%{_includedir}/utlist.h
%{_includedir}/utstring.h

