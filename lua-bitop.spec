#
# Conditional build:
%bcond_without	tests		# build without tests

%define	__lua	/usr/bin/lua5.1
%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
Summary:	C extension module for Lua which adds bitwise operations on numbers
Name:		lua-bitop
Version:	1.0.2
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://bitop.luajit.org/download/LuaBitOp-%{version}.tar.gz
# Source0-md5:	d0c1080fe0c844e8477279668e2d0d06
URL:		http://bitop.luajit.org/
BuildRequires:	lua51 >= %{luaver}
BuildRequires:	lua51-devel >= %{luaver}
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lua BitOp is a C extension module for Lua 5.1/5.2 which adds bitwise
operations on numbers.

Supported functions: bit.tobit, bit.tohex, bit.bnot, bit.band,
bit.bor, bit.bxor, bit.lshift, bit.rshift, bit.arshift, bit.rol,
bit.ror, bit.bswap

%prep
%setup -q -n LuaBitOp-%{version}

%build
%{__make} all %{?with_tests:test} \
	INCLUDES=$(pkg-config --cflags lua%{luaver}) \
	LUA="%{__lua}" \
	CCOPT="%{rpmcflags} -fomit-frame-pointer" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{lualibdir}
install -p bit.so $RPM_BUILD_ROOT%{lualibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* doc/*
%attr(755,root,root) %{lualibdir}/bit.so
