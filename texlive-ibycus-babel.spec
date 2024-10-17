Name:		texlive-ibycus-babel
Version:	15878
Release:	2
Summary:	Use the Ibycus 4 Greek font with Babel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/greek/ibycus-babel
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ibycus-babel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ibycus-babel.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ibycus-babel.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to use the Ibycus 4 font for ancient
Greek with Babel. It uses a Perl script to generate hyphenation
patterns for Ibycus from those for the ordinary Babel encoding,
cbgreek. It sets up "ibycus" as a pseudo-language you can
specify in the normal Babel manner. For proper hyphenation of
Greek quoted in mid-paragraph, you should use it with elatex.
See the README for details.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
