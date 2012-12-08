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
Release:	%mkrel 6
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




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.4.0-4mdv2011.0
+ Revision: 662877
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.4.0-3mdv2011.0
+ Revision: 603469
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.4.0-2mdv2010.1
+ Revision: 518970
- rebuild

* Wed Jun 24 2009 Isabel Vallejo <isabel@mandriva.org> 1:1.4.0-1mdv2010.0
+ Revision: 388880
- update to 1.4.0
- update to 1.4.0

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1:0.60.0-5mdv2009.1
+ Revision: 350126
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1:0.60.0-4mdv2009.0
+ Revision: 220457
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 1:0.60.0-3mdv2008.1
+ Revision: 182663
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1:0.60.0-2mdv2008.1
+ Revision: 148868
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-1mdv2007.0
+ Revision: 123382
- Import aspell-uk

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-1mdv2007.1
- use the mkrel macro
- disable debug packages

* Mon Nov 28 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.60.0-1mdk
- new release (thus saving 5Mb on CDs)

* Tue Oct 04 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.51.0-4mdk
- should not be a noarch packag

* Fri Dec 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.51.0-3mdk
- rebuild for new aspell

* Wed Jul 28 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.51.0-2mdk
- allow build on ia64

