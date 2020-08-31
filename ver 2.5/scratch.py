#PYQT5에서 드래그앤 드랍으로 경우의 수 나오게 하기
#두 개이상 선택이 가능하게 하는 경우를 CREATE로 만들기(파이썬에서 swithcase문 쓸 수 없으니까... dictionary 써야 하나)

#LINEAGE 4 / PATIENT 2 / CELL LINE 4 (create_list안에) --> 8+8+16+32...(일단은 colon을 제외한 경우를 따져야할 듯)
#아래쪽에 첨부하기

def create_analysis(idx) :
    cases_of_creation = {
        1: 'survival_drug';
        2: 'survival_CRISPR';
        3: 'survival_shRNA';
        4: 'survival_mRNA';
        5: 'mRNA_drug';
        6: 'mRNA_CRISPR';
        7: 'mRNA_shRNA';
        8: 'mRNA_mRNA';
        #combination of 'patient_cellline'
    }
    return cases_of_creation.get(idx, '{} is invalid index (1-8)'.format(idx))

create_analysis(1)
create_analysis(2)
create_analysis(3)
create_analysis(4)
create_analysis(5)
create_analysis(6)
create_analysis(7)
create_analysis(8)



#일단 이 코드에서 patient와 cellline의 조건을 먼저 분리해주었으므로 그 다음에 이어질 때 콤보박스로 colon울 선택하든지..
#아니면 그냥 lineage자체를 먼저 선택하게 한 다음에 나머지를 선택해야 빨라지는 건지....
