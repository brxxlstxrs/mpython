 
set encoding=utf-8
set number relativenumber
set cc=81
"set background=dark

set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
"set smarttab
set autoindent
set updatetime=300

call plug#begin()
  Plug 'neoclide/coc.nvim', {'branch': 'release'} 
  Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
  Plug 'junegunn/fzf.vim'
  Plug 'preservim/nerdtree'
  Plug 'preservim/nerdcommenter'
  Plug 'morhetz/gruvbox'
"  Plug 'ap/vim-css-color'
  Plug 'vim-airline/vim-airline'
  Plug 'vim-airline/vim-airline-themes'
  Plug 'ryanoasis/vim-devicons'
  Plug 'jiangmiao/auto-pairs'
  Plug 'airblade/vim-gitgutter'
  Plug 'tpope/vim-fugitive'
call plug#end()

colorscheme gruvbox

let g:airline#extensions#tabline#enabled = 1
let g:airline_powerline_fonts = 1
"let g:airline#extensions#tabline#left_sep = ' '
let g:airline#extensions#tabline#left_alt_sep = '|'
"let g:airline#extensions#tabline#formatter = 'unique_tail_improved'


