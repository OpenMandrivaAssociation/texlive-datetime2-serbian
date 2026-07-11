%global tl_name datetime2-serbian
%global tl_revision 67201

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1.0
Release:	%{tl_revision}.1
Summary:	Serbian language module for the datetime2 package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/datetime2-contrib/datetime2-serbian
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-serbian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-serbian.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-serbian.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This module provides the "serbian" style that can be set using
\DTMsetstyle provided by datetime2.sty. It provides both Cyrillic and
Latin, Ekavian and Ijekavian variants of Serbian date formats,
regionalized and non-regionalized.

