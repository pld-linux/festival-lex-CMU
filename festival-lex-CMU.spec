Summary:	American English Lexicon
Summary(pl):	Leksyka ameryka�skiej odmiany j�zyka angielskiego
Name:		festival-lex-CMU
Version:	0.4
Release:	1
License:	Distributable
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/download/festival/1.4.2/festlex_CMU.tar.gz
Requires:	festival-lex-POS
Provides:	festival-lex-english
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains an American English Lexicon and letter to sound
rules based on CMUDICT 0.4.

%description -l pl
Ten pakiet zawiera leksyk� ameryka�skiej odmiany j�zyka angielskiego
i zasady konwersji liter na d�wi�ki bazowane na CMUDICT 0.4.

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