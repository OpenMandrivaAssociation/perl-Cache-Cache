%define upstream_name    Cache-Cache
%define upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Cache/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Digest::SHA1) >= 2.02
BuildRequires:	perl(Error) >= 0.15
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl(IPC::ShareLite) >= 0.09
BuildRequires:	perl(Storable) >= 1.014
BuildArch:	noarch
Requires: 	perl(Digest::SHA1) >= 2.02
Requires:	perl(Error) >= 0.15
Requires:	perl(IPC::ShareLite) >= 0.09
Requires:	perl(Storable) >= 1.014

%description
Cache-Cache module for perl.  The Cache modules are designed to assist
a developer in persisting data for a specified period of time.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%defattr(444,root,root,755)
%doc CHANGES COPYING CREDITS DISCLAIMER README STYLE
%{_mandir}/*/*
%{perl_vendorlib}/Cache


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.60.0-2mdv2011.0
+ Revision: 680709
- mass rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.60.0-1mdv2011.0
+ Revision: 402985
- rebuild using %%perl_convert_version

* Mon Mar 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdv2009.1
+ Revision: 346987
- update to new version 1.06

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.05-2mdv2008.1
+ Revision: 136666
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-2mdv2008.0
+ Revision: 85922
- rebuild


* Fri May 26 2006 Scott Karns <scottk@mandriva.org> 1.05-1mdv2007.0
- 1.05

* Fri May 19 2006 Scott Karns <scottk@mandriva.org> 1.04-4mdk
- Fixed BuildRequires perl(Storable) typo

* Fri May 19 2006 Scott Karns <scottk@mandriva.org> 1.04-3mdk
- Updated requires and buildrequires
- Added check section

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.04-2mdk
- fix buildrequires

* Mon May 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.04-1mdk
- 1.04

* Sat Apr 16 2005 Oden Eriksson <oeriksson@mandriva.com> 1.03-2mdk
- fix deps

* Tue Oct 12 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.03-1mdk
- 1.03
- add "make test"

* Thu Sep 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.02-4mdk
- rebuild

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.02-3mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- don't use PREFIX
- ues %%makeinstall_std macro

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.02-2mdk
- rebuild for new auto{prov,req}

