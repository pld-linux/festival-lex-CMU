Summary:	American English Lexicon
Summary(pl.UTF-8):	Leksyka amerykańskiej odmiany języka angielskiego
Name:		festival-lex-CMU
# see festival/lib/dicts/cmu/cmulex.scm /cmulex_version
Version:	2.0
Release:	1
License:	distributable
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/downloads/festival/2.4/festlex_CMU.tar.gz
# Source0-md5:	6a2ee4fed7c3ebedf197a3b8524ccb87
URL:		http://www.cstr.ed.ac.uk/projects/festival/
Requires:	festival-lex-POS
Provides:	festival-lex-english
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains an American English Lexicon and letter to sound
rules based on CMUDICT 0.4.

%description -l pl.UTF-8
Ten pakiet zawiera leksykę amerykańskiej odmiany języka angielskiego
i zasady konwersji liter na dźwięki bazowane na CMUDICT 0.4.

%prep
%setup -q -c

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
