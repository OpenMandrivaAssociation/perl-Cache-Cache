%define upstream_name    Cache-Cache
%define upstream_version 1.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary: 	%{upstream_name} module for perl
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url: 		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Cache/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(Digest::SHA1) >= 2.02
BuildRequires:	perl(Error) >= 0.15
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl(IPC::ShareLite) >= 0.09
BuildRequires:	perl(Storable) >= 1.014
BuildArch: 	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires: 	perl-Digest-SHA1 >= 2.02
Requires:	perl-Error >= 0.15
Requires:	perl-IPC-ShareLite >= 0.09
Requires:	perl-Storable >= 1.0.14

%description
Cache-Cache module for perl.  The Cache modules are designed to assist
a developer in persisting data for a specified period of time.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorlib}/Cache
