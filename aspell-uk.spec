%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 1.4.0-0
%define languagelocal uk
%define languageeng ukrainian
%define languageenglazy Ukrainian
%define languagecode uk
%define lc_ctype en_UK

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Epoch:		1
Version:	1.4.0_0
Release:	1
Group:		System/Internationalization
License:	GPLv2+ and LGPLv2+
Url:		https://aspell.sourceforge.net/
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell6-%{languagecode}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= 0.60
Requires:	aspell >= 0.60
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	spell-%{languagecode}
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn aspell6-%{languagecode}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

# fix doc perms
chmod 644 README* Copyright

%files
%doc README* Copyright
%{_libdir}/aspell-*/*

