#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Cwd
%define		pnam	Guard
Summary:	Cwd::Guard - temporary changing working directory (chdir)
Summary(pl.UTF-8):	Cwd::Guard - tymczasowa zmiana katalogu roboczego (chdir)
Name:		perl-Cwd-Guard
Version:	0.05
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Cwd/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3d9c31722ab475fcb095716fe80c6bb1
URL:		https://metacpan.org/dist/Cwd-Guard
BuildRequires:	perl-Module-Build >= 0.38
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cwd::Guard can change the current directory (chdir) using a limited
scope.

%description -l pl.UTF-8
Cwd::Guard pozwala zmienić bieżący katalog (chdir) w ograniczonym
kontekście.

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
%dir %{perl_vendorlib}/Cwd
%{perl_vendorlib}/Cwd/Guard.pm
%{_mandir}/man3/Cwd::Guard.3pm*
