Summary:	Tamil dictionary for aspell
Summary(pl.UTF-8):   Słownik tamilski dla aspella
Name:		aspell-ta
Version:	20040424
%define	subv	1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/ta/aspell6-ta-%{version}-%{subv}.tar.bz2
# Source0-md5:	fc98b0b8d79291448d3a4f48ebbf2bd0
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tamil dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik tamilski (lista słów) dla aspella.

%prep
%setup -q -n aspell6-ta-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
