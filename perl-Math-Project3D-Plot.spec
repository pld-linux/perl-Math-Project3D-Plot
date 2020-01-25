#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Math
%define	pnam	Project3D-Plot
Summary:	Math::Project3D::Plot - Perl extension for plotting projections of 3D functions
Summary(pl.UTF-8):	Math::Project3D::Plot - rozszerzenie Perla do rysowania rzutów funkcji 3D
Name:		perl-Math-Project3D-Plot
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2ac47684734a31f349ecd11d195a87c5
URL:		http://search.cpan.org/dist/Math-Project3D-Plot/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Imager >= 0.41
BuildRequires:	perl-Math-Project3D >= 1.02
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module may be used to plot the results of a projection from a
three dimensional vectorial function onto a plane into an image. What
a horrible sentence.

%description -l pl.UTF-8
Ten moduł służy do rysowania wyniku rzutu trójwymiarowej funkcji
wektorowej na powierzchnię na obrazie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/Project3D/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
