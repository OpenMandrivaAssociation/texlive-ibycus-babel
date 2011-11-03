# revision 15878
# category Package
# catalog-ctan /language/greek/ibycus-babel
# catalog-date 2009-05-06 13:52:38 +0200
# catalog-license lppl
# catalog-version 3.0
Name:		texlive-ibycus-babel
Version:	3.0
Release:	1
Summary:	Use the Ibycus 4 Greek font with Babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/greek/ibycus-babel
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ibycus-babel.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ibycus-babel.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ibycus-babel.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package allows you to use the Ibycus 4 font for ancient
Greek with Babel. It uses a Perl script to generate hyphenation
patterns for Ibycus from those for the ordinary Babel encoding,
cbgreek. It sets up "ibycus" as a pseudo-language you can
specify in the normal Babel manner. For proper hyphenation of
Greek quoted in mid-paragraph, you should use it with elatex.
See the README for details.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ibycus-babel/ibycus.ldf
%{_texmfdistdir}/tex/latex/ibycus-babel/lgienc.def
%{_texmfdistdir}/tex/latex/ibycus-babel/lgifib.fd
%doc %{_texmfdistdir}/doc/latex/ibycus-babel/README
%doc %{_texmfdistdir}/doc/latex/ibycus-babel/ibycus-babel-test.tex
%doc %{_texmfdistdir}/doc/latex/ibycus-babel/ibycus-babel.pdf
%doc %{_texmfdistdir}/doc/latex/ibycus-babel/ibyhyph.pl
#- source
%doc %{_texmfdistdir}/source/latex/ibycus-babel/ibycus-babel.dtx
%doc %{_texmfdistdir}/source/latex/ibycus-babel/ibycus-babel.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
