%global tl_name attachfile2
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.12
Release:	%{tl_revision}.1
Summary:	Attach files into PDF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/attachfile2
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/attachfile2.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/attachfile2.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/attachfile2.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(attachfile2.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package can be used to attach files to a PDF document. It is a
further development of Scott Pakin's package attachfile for pdfTeX.
Apart from bug fixes, this package adds support for dvips, some new
options, and gets and writes meta information data about the attached
files.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/scripts
%dir %{_datadir}/texmf-dist/texmf-dist/source
%dir %{_datadir}/texmf-dist/texmf-dist/tex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man
%dir %{_datadir}/texmf-dist/texmf-dist/scripts/attachfile2
%dir %{_datadir}/texmf-dist/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/latex/attachfile2
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man/man1
%dir %{_datadir}/texmf-dist/texmf-dist/source/latex/attachfile2
%dir %{_datadir}/texmf-dist/texmf-dist/tex/latex/attachfile2
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/attachfile2/README.md
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/attachfile2/attachfile2.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/pdfatfi.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/pdfatfi.man1.pdf
%{_datadir}/texmf-dist/texmf-dist/scripts/attachfile2/pdfatfi.pl
%doc %{_datadir}/texmf-dist/texmf-dist/source/latex/attachfile2/attachfile2.dtx
%{_datadir}/texmf-dist/texmf-dist/tex/latex/attachfile2/atfi-dvipdfmx.def
%{_datadir}/texmf-dist/texmf-dist/tex/latex/attachfile2/atfi-dvips.def
%{_datadir}/texmf-dist/texmf-dist/tex/latex/attachfile2/atfi-luatex.def
%{_datadir}/texmf-dist/texmf-dist/tex/latex/attachfile2/atfi-pdftex.def
%{_datadir}/texmf-dist/texmf-dist/tex/latex/attachfile2/attachfile2.sty
