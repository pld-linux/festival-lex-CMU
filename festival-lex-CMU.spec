Summary:	American English Lexicon
Summary(pl):	Leksyka amerykañskiej odmiany jêzyka angielskiego
Name:		festival-lex-CMU
Version:	0.4
Release:	3
License:	distributable
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/download/festival/1.4.3/festlex_CMU.tar.gz
# Source0-md5:	a3ffcd09dcbf1306fdef3c84c1c521d6
Requires:	festival-lex-POS
Provides:	festival-lex-english
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains an American English Lexicon and letter to sound
rules based on CMUDICT 0.4.

%description -l pl
Ten pakiet zawiera leksykê amerykañskiej odmiany jêzyka angielskiego
i zasady konwersji liter na d¼wiêki bazowane na CMUDICT 0.4.

%prep
%setup -q -c %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/festival/lib/dicts/cmu

cd festival/lib/dicts/cmu
install cmulex.scm cmu_lts_rules.scm cmudict-0.4.out \
		$RPM_BUILD_ROOT%{_datadir}/festival/lib/dicts/cmu

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc festival/lib/dicts/cmu/COPYING
%{_datadir}/festival/lib/dicts/cmu
