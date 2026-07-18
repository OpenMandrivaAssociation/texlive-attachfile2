%global tl_name attachfile2
%global tl_revision 79461
%global tl_bin_links pdfatfi:%{_texmfdistdir}/scripts/attachfile2/pdfatfi.pl

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
BuildSystem:	texlive
Requires:	texlive(attachfile2.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
This package can be used to attach files to a PDF document. It is a
further development of Scott Pakin's package attachfile for pdfTeX.
Apart from bug fixes, this package adds support for dvips, some new
options, and gets and writes meta information data about the attached
files.

