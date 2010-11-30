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
Version:	1.4.0
Release:	%mkrel 3
Group:		System/Internationalization
Source:	    http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell6-%{languagecode}-%{src_ver}.tar.bz2
URL:		http://aspell.sourceforge.net/
License:	GPLv2+ and LGPLv2+
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires:	aspell >= 0.60
Requires:	aspell >= 0.60

# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
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
chmod 644 README* Copyright

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright
%{_libdir}/aspell-*/*


