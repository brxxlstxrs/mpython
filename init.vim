" Let's make it beautiful
set number
set cc=81
set background=dark
set termguicolors

" Tab settings 
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set autoindent

" Basic settings 
set encoding=utf-8
set updatetime=100
set hidden
set nobackup
set nowritebackup
set noswapfile

" Plugins 
call plug#begin()
  Plug 'neoclide/coc.nvim', {'branch': 'release'} 
  Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
  Plug 'junegunn/fzf.vim'
  Plug 'preservim/nerdtree'
  Plug 'preservim/nerdcommenter'
  Plug 'vim-airline/vim-airline'
  Plug 'vim-airline/vim-airline-themes'
  Plug 'ryanoasis/vim-devicons'
  Plug 'jiangmiao/auto-pairs'
  Plug 'airblade/vim-gitgutter'
  Plug 'tpope/vim-fugitive'
  Plug 'sainnhe/gruvbox-material'
  Plug 'joshdick/onedark.vim'
call plug#end()

" Coc settings 
let g:coc_global_extensions = [
        \'coc-pyright']

" other settings
let g:gruvbox_material_palette = 'mix'
let g:gruvbox_material_disable_italic_comment = 1
let g:airline#extensions#tabline#enabled = 1
" let g:airline_powerline_fonts = 1

" set colorscheme
colorscheme gruvbox-material
