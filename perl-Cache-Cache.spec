%define module  Cache-Cache
%define	modprefix Cache

%define version 1.05

%define	rel	2
%define release %mkrel %{rel}

Summary: 	%{module} module for perl
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
Url: 		http://search.cpan.org/dist/%{module}
BuildArch: 	noarch
Requires: 	perl-Digest-SHA1 >= 2.02
Requires:	perl-Error >= 0.15
Requires:	perl-IPC-ShareLite >= 0.09
Requires:	perl-Storable >= 1.0.14
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(Digest::SHA1) >= 2.02
BuildRequires:	perl(Error) >= 0.15
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl(IPC::ShareLite) >= 0.09
BuildRequires:	perl(Storable) >= 1.014
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Cache-Cache module for perl.  The Cache modules are designed to assist
a developer in persisting data for a specified period of time.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(444,root,root,755)
%doc CHANGES COPYING CREDITS DISCLAIMER README STYLE
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}

