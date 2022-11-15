Name:		texlive-attachfile2
Version:	57959
Release:	1
Summary:	Attach files into PDF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/attachfile2
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/attachfile2.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/attachfile2.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/attachfile2.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package can be used to attach files to a PDF document. It
is a further development of Scott Pakin's package attachfile
for pdfTeX. Apart from bug fixes, this package adds support for
dvips, some new options, and gets and writes meta information
data about the attached files.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/source/latex/attachfile2
%{_texmfdistdir}/tex/latex/attachfile2
%{_texmfdistdir}/scripts/attachfile2
%doc %{_texmfdistdir}/doc/latex/attachfile2
%doc %{_texmfdistdir}/doc/man/man1/*

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
