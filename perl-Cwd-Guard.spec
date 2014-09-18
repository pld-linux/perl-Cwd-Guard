#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Cwd
%define		pnam	Guard
%include	/usr/lib/rpm/macros.perl
Summary:	Cwd::Guard - Temporary changing working directory (chdir)
Name:		perl-Cwd-Guard
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Cwd/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	26d12d3e4313943c7754afeec0f6462c
URL:		http://search.cpan.org/dist/Cwd-Guard/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CORE::chdir Cwd:: Guard can change the current directory (chdir)
using a limited scope.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Cwd/*.pm
%{_mandir}/man3/*
