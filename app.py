import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("?? �J���t���~�O���t�W�F�l���[�^�[")

st.write("�ȉ��̃X���C�_�[�ō��ڐ���I��ł�������??")

num_sections = st.slider("���ڐ�", min_value=2, max_value=10, value=5)

# �����_���Ȋ����ƃ��x�����쐬
values = np.random.rand(num_sections)
values /= values.sum()
labels = [f"���� {i+1}" for i in range(num_sections)]

# �O���t�`��
fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
ax.axis("equal")

st.pyplot(fig)
