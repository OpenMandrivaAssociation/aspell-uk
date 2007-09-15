%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 1.1-0
%define languagelocal uk
%define languageeng ukrainian
%define languageenglazy Ukrainian
%define languagecode uk
%define lc_ctype en_UK

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.60.0
Release:	%mkrel 1
Group:		System/Internationalization
Source:	    http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell6-%{languagecode}-%{src_ver}.tar.bz2
URL:		http://aspell.sourceforge.net/
License:	GPL
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires:	aspell >= 0.50
Requires:	aspell >= 0.50

# Mandriva Stuff
Requires:	locales-%{languagecode}
Provides:	aspell-dictionary

Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n aspell6-%{languagecode}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

# fix doc perms
chmod 644 README* Copyright doc/*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright doc/*
%{_libdir}/aspell-*/*


