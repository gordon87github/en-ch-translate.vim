"execute vim internal command py or py3 to execute python module
exec g:python_vim_cmd . 'import vim'
exec g:python_vim_cmd . 'import sys'
exec g:python_vim_cmd . 'cwd = vim.eval("expand(\"<sfile>:p:h\")")'
exec g:python_vim_cmd . 'sys.path.insert(0,cwd)'
exec g:python_vim_cmd . 'from TranslateUtil import search'

function! search#SearchExplain(word)
	exec g:python_vim_cmd . 'search.searchExplain()'
endfunction

function! search#SearchExplainAction(type)
	if a:0
		execute "normal! gvy"
	elseif a:type == "line"
		execute "normal! '[V']y"
	else
		execute "normal! `[v`]y"
	endif
	echom @@
endfunction
